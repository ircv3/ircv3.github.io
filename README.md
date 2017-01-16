# IRCv3 Website

This is the IRCv3 website.

## Testing

If you want to test your changes to this website locally before submitting a pull request (always a good idea), there are two options.

After you finish those steps, you will be able to go to [http://127.0.0.1:4000/](http://127.0.0.1:4000/) and view a local copy of the website. As you make changes to your files, they will be reflected on that local copy.

### Using [Bundler](https://bundler.io/):

1. `git clone` this repository
2. `cd ircv3.github.io/`
3. `git submodule update --init --recursive`
4. `bundle install`
5. `bundle exec jekyll serve`

### Manually

You should make sure your manually installed local versions should match that of [GitHub Pages](https://pages.github.com/versions/):

1. Install [Jekyll](https://jekyllrb.com/)
2. Install `jekyll-sitemap` with `gem install jekyll-sitemap`
3. `git clone` this repository
4. `cd ircv3.github.io/`
5. `git submodule update --init --recursive`
6. `jekyll serve`

## Licenses

The RSS XML feed template was sourced from the [Jekyll RSS Feed Templates](https://github.com/snaptortoise/jekyll-rss-feeds) repo, and is used under this MIT license:

The MIT License (MIT)

Copyright (c) 2014 George Mandis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
