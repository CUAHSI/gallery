#!/usr/bin/env python

import os
import yaml
import shutil
import base64
import jinja2
import requests
import argparse
from lxml import etree
from termcolor import colored


# global vars
source_dir = "./source"
gallery_dir = f"./source/gallery"
template_dir = f"./source/_templates"
static_dir = f"./source/_static"


def render_page(template, data, outpath="./index.rst"):
    Loader = jinja2.FileSystemLoader(searchpath="./")
    env = jinja2.Environment(loader=Loader)
    template = env.get_template(template)

    text = template.render(data)
    with open(outpath, "w") as f:
        f.write(text)


def get_metadata_from_hs(hsguid):
    """
    This function collects metadata from a hydroshare resource
    """
    data = {}
    try:
        r = requests.get(f"https://hydroshare.org/hsapi/resource/{hsguid}/scimeta")
        if r.status_code != 200:
            raise Exception

        # encode response as bytestring
        txt = r.text.encode()

        # parse into lxml object
        root = etree.fromstring(txt)
        creators = root.findall(".//dc:creator", root.nsmap)
        data["authors"] = []

        for creator in creators:
            terms = creator.find("rdf:Description", root.nsmap)
            d = {}
            for att in ["name", "organization", "email"]:
                val = terms.find(f"hsterms:{att}", root.nsmap)
                if val is not None:
                    d[att] = val.text

            # save the user's profile page if it exists
            user_url = terms.find(f'hsterms:description',root.nsmap)
            if user_url is not None:
                d['hs-profile'] = f'https://hydroshare.org{user_url.text}'

            data["authors"].append(d)

        # get the resource title and description
        data["title"] = root.find(".//dc:title", root.nsmap).text

        # todo: the encoding of description does not preserve newlines.
        data["description"] = (
            root.find(".//dcterms:abstract", root.nsmap)
            .text.encode("ascii", "ignore")
            .decode()
        )

        # get the keywords
        subject_kw = root.findall("rdf:Description/dc:subject", root.nsmap)
        keywords = [kw.text for kw in subject_kw]
        if len(keywords) > 0:
            data["keywords"] = keywords

    except Exception:
        print(f"Failed to get hydroshare data for resource id: {hsguid}")
        return None

    return data


def copy_static(data):
    """
    copy static files to _static directory
    """
    print('   copying static files ', end='')
    if 'thumbnail' in data.keys():
        # move thumbnail to _static and rename it
        thumbnail_path = os.path.abspath(
            os.path.join(subdir, data["thumbnail"])
        )
        if os.path.exists(thumbnail_path):
            thumbnail_new_name = f'thumbnail-{data["label"]}'
            shutil.copyfile(thumbnail_path, f"{static_dir}/{thumbnail_new_name}")
            data["thumbnail"] = thumbnail_new_name
            print(colored('\u2713', 'green'))
            return data

    # set thumbnail using the default "unknown" image
    print(colored('\ufffd', 'yellow'))
    print('   '+colored('WARNING: Missing thumbnail, using default image',
                        'yellow'))
    data['thumbnail'] = 'missing-thumbnail.png'

    return data


def write_yaml_cache(outdir, data, filename='.cache.yaml'):
    """
    saves data to yaml file
    outdir: directory to save file
    filename: name of file, default .cache.yaml
    data: dictionary of data to save
    """

    with open(os.path.join(outdir, filename), 'w') as f:
        yaml.dump(data, f)


def build_example_page(example_path):
    """
    creates example landing page from a conf.yaml file
    example_path: full path to conf.yaml file
    returns: dictionary of data for the example or None
    """
    print(f'\n-- building example {os.path.basename(example_path)[0:50]}...')
    conf = os.path.join(example_path, "conf.yaml")
    with open(conf, "r") as f:
        # load yaml data
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)

        hsdata = None
        hsid = yaml_data.get("hydroshare", {}).get("id")
        # collect hydroshare data if a resource id is provided
        # in the yaml file
        if hsid is not None:
            # load data from hydroshare
            print('   collecting data from HydroShare ', end='')
            hsdata = get_metadata_from_hs(hsid)
            if hsdata is None:
                print(colored('\u2717', 'red'))
                print('   '+colored('ERROR: something bad happened, skipping',
                      'red'))
                # exit early
                return None
            print(colored('\u2713', 'green'))
            


        # combine hsdata and yaml data.
        # note, yaml data will overwrite hs data
        data = hsdata or {}
        data.update(yaml_data)

        # make sure a page label exists in data. If not, create one.
        if "label" not in data.keys():
            try:
                # set the label as the HS id if it exists
                data['label'] = data['hydroshare']['id']
            except Exception:
                # set to a base64 encoding of the title
                data['label'] = base64.b64encode(data['title'].encode()).decode()

        # clean newlines from description
        data['description'] = data['description'].replace('\n', '')
        data['description'] = data['description'].replace('\r', '<br>')

        # set the short-title and short-description if they're provided
        # otherwise use regular title and description. These are displayed
        # on the example html cards.
        if data.get('short_description', None) is None:
            data['short_description'] = (data['description'][0:150] + '...'
                                         if len(data['description']) > 150
                                         else data['description'][0:150])
        if data.get('short_title', None) is None:
            data['short_title'] = (data['title'][0:50] + '...'
                                   if len(data['title']) > 150
                                   else data['title'])

        # save the configuration data to a .cache.yaml file
        # so the site can be re-build without querying metadata
        # from HydroShare every time.
        print('   writing cache ', end='')
        write_yaml_cache(subdir, data, filename='.cache.yaml')
        print(colored('\u2713', 'green'))

        print('   creating rST file ', end='')
        # write the rST page for this example
        render_page(
            os.path.join(template_dir, "landingpage.rst"),
            data,
            outpath=os.path.join(subdir, "index.rst"),
        )
        print(colored('\u2713', 'green'))
        return data


def build_example_page_cache(example_path):
    """
    creates example landing page from a .cache.yaml file
    example_path: full path to example that will be rendered
    returns: dictionary of data for the example or None
    """
    try:
        print('\n' + os.path.basename(example_path))
        print('.. building from cache')
        cache_conf = os.path.join(example_path, '.cache.yaml')
        with open(cache_conf, "r") as f:
            # load yaml data
            data = yaml.load(f, Loader=yaml.FullLoader)

            # write the rST page for this example
            render_page(
                os.path.join(template_dir, "landingpage.rst"),
                data,
                outpath=os.path.join(subdir, "index.rst"),
            )
            
            return data
    except Exception:
        print('   ' + colored('ERROR reading cache. I will try building '
                              'without cache', 'red'))
        return None


def build_subgallery_pages(conf):
    """
    Builds each sub-gallery page, consisting of categories and html
    cards for each example.
    """

    # build the sub-gallery pages
    with open(conf, "r") as f:
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)

        print('\n.. building sub-gallery pages')

        # build the sub-gallery pages
        gallery_labels = {}
        for sub, sub_data in subgalleries.items():
            # create a label for the subgallery page
            # set to a base64 encoding of the title
            print(f'   processing {sub} ', end='')
            subname = os.path.basename(sub)
            id = base64.b64encode(subname.encode()).decode()
            gallery_labels[sub] = id

            # generate page title. This is necessary for the TOC
            # get the title from the top-level conf if it exists,
            # otherwise get it from the directory name
            title = None
            for v in yaml_data["galleries"]:
                if sub == v['gallery_path']:
                    title = v['display_name']
                    break
            if title is None:
                title = f"{os.path.basename(sub)} Gallery"

            render_page(
                os.path.join(template_dir, "gallery.rst"),
                {"label": id, "gallery_title": title, "categories": sub_data},
                outpath=os.path.join(sub, "index.rst"),
            )
            print(colored('\u2713', 'green'))

    return yaml_data, gallery_labels


def build_homepage_panels(yaml_data, gallery_labels):

    homepage_panels = []
    print('\n.. building homepage panels')
    for v in yaml_data["galleries"]:
        if v["gallery_path"] in gallery_labels:
            print(f'   processing {v["display_name"]} ', end='')
            v["label"] = gallery_labels[v["gallery_path"]]

            # only render galleries on the homepage that have labels. 
            # this will ignore any galleries defined in conf.yaml that
            # do not have rendered example pages.
            homepage_panels.append(v)
            print(colored('\u2713', 'green'))
            
    render_page(
        os.path.join(template_dir, "homepage.rst"),
        {'galleries': homepage_panels},
        outpath=os.path.join(source_dir, "index.rst"),
    )


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument(
        "-g",
        "--gallery",
        default=gallery_dir,
        help=f"path of the gallery to build, if nothing is provided all galleries in {gallery_dir} will be built.",
    )
    p.add_argument('--cache', action='store_true', default=False,
                   help='indicates that cache files should be used if they exist, useful for rebuilding the pages without recollecting metadata from external sources, e.g. HydroShare')
    args = p.parse_args()

    # loop through each directory in the gallery
    # only process directories that contain conf.yaml files,
    # ignore all other directories
    subgalleries = {}
    for subdir, dirs, files in os.walk(args.gallery):
        if "conf.yaml" in files:

            # build from cache if --cache flag is provided. If a cache file
            # isn't found, proceed to build without cache.
            data = None
            if args.cache:
                data = build_example_page_cache(subdir)
            if data is None:
                data = build_example_page(subdir)

            # save the sub-gallery and category if the example was
            # build successfully
            if data is not None:

                # move static data
                data = copy_static(data)

                # save this metadata for the sub-gallery page too
                subgallery_path = os.path.dirname(os.path.dirname(subdir))
                category = os.path.basename(os.path.dirname(subdir))

                # add the sub-gallery to a dictionary if it doesn't already
                # exist. This dictionary will be used to build the sub-gallery
                # pages. Do the same for the categories which will be rendered
                # on the gallery homepage.
                if subgallery_path not in subgalleries.keys():
                    subgalleries[subgallery_path] = {}
                if category not in subgalleries[subgallery_path].keys():
                    subgalleries[subgallery_path][category] = []
                subgalleries[subgallery_path][category].append(data)

    # build the sub-gallery pages
    subgallery_conf = os.path.join(source_dir, "conf.yaml")
    yaml_data, gallery_labels = build_subgallery_pages(subgallery_conf)

    # build the homepage panels
    build_homepage_panels(yaml_data, gallery_labels)
