#!/usr/bin/env python

import os
import yaml
import jinja2
import argparse


# global vars
source_dir = './source'
gallery_dir = './source/gallery'
template_dir = './source/_templates'

def build_page_data(yamlfile):

    return data

def render_page(template, data, outpath='./index.rst'):
    Loader = jinja2.FileSystemLoader(searchpath="./")
    env = jinja2.Environment(loader=Loader)
    template = env.get_template(template)

    text = template.render(data)
    with open(outpath, 'w') as f:
        f.write(text)


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
#            import pdb; pdb.set_trace()
            print(f'processing: {subdir}')
            with open(conf, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                render_page(os.path.join(template_dir, 'landingpage.rst'),
                            data,
                            outpath=os.path.join(subdir, 'index.rst'))




