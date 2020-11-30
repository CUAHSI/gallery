#!/usr/bin/env python

import os
import yaml
import jinja2
import requests
import argparse
from lxml import etree


# global vars
source_dir = './source'
gallery_dir = './source/gallery'
template_dir = './source/_templates'

def render_page(template, data, outpath='./index.rst'):
    Loader = jinja2.FileSystemLoader(searchpath="./")
    env = jinja2.Environment(loader=Loader)
    template = env.get_template(template)

    text = template.render(data)
    with open(outpath, 'w') as f:
        f.write(text)

def get_metadata_from_hs(hsguid):
    """
    This function collects metadata from a hydroshare resource
    """
    data = {}
    try:
        r = requests.get(f'https://hydroshare.org/hsapi/resource/{hsguid}/scimeta')
        if r.status_code != 200:
            raise Exception

        # parse the response
        root = etree.fromstring(r.text)

        creators = root.findall('rdf:Description/dc:creator', root.nsmap)
        data['authors'] = []
        for creator in creators:
            terms = creator.find('rdf:Description', root.nsmap)
            d = {}
            for att in ['name', 'organization', 'email']:
                val = terms.find(f'hsterms:{att}', root.nsmap)
                if val is not None:
                    d[att] = val.text
            about = f'{{{root.nsmap["rdf"]}}}about'
            if about in terms.attrib:
                d['url'] = terms.attrib[about]
            data['authors'].append(d)

        # get the resource title and description
        data['title'] = root.find('rdf:Description/dc:title', root.nsmap).text

        # todo: the encoding of description does not preserve newlines.
        data['description'] = root.find('rdf:Description/dc:description/rdf:Description/dcterms:abstract', root.nsmap).text.encode('ascii', 'ignore').decode()

        # get the keywords
        subject_kw = root.findall('rdf:Description/dc:subject', root.nsmap)
        keywords = [kw.text for kw in subject_kw]
        if len(keywords) > 0:
            data['keywords'] = keywords

    except:
        print(f'Failed to get hydroshare data for resource id: {hsguid}')
        return None

    return data

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-g', '--gallery', default=gallery_dir,
                   help=f'path of the gallery to build, if nothing is provided all galleries in {gallery_dir} will be built.')

    args = p.parse_args()

##    import pdb; pdb.set_trace()
#    if args.gallery is not None:
#        galleries = [os.path.join(gallery_dir, args.gallery)]
#    else:
#        galleries = [f for f in os.listdir(gallery_dir) if not f.startswith('.')]
#
#    # loop through each gallery and build pages for each example
#    for gallery in galleries:
#        categories = [d for d in os.listdir(gallery) if os.path.isdir(os.path.join(gallery, d))]
#        for category in categories:
#            print(f'processing: {os.path.join(gallery, category)}')
#            examples = [d for d in os.listdir(gallery) if os.path.isdir(os.path.join(gallery, d))]
#            for example in 

    for subdir, dirs, files in os.walk(args.gallery):
        if 'conf.yaml' in files:
            conf = os.path.join(subdir, 'conf.yaml')
            print(f'processing: {subdir}')
            with open(conf, 'r') as f:
                # load yaml data
                yaml_data = yaml.load(f, Loader=yaml.FullLoader)

                hsdata = None
                hsid = yaml_data.get('hydroshare', {}).get('id')
                if hsid is not None:
                    # load data from hydroshare
                    hsdata = get_metadata_from_hs(hsid)

                # combine hsdata and yaml data.
                # note, yaml data will overwite hs data
                data = hsdata or {}
                data.update(yaml_data)

                render_page(os.path.join(template_dir, 'landingpage.rst'),
                            data,
                            outpath=os.path.join(subdir, 'index.rst'))




