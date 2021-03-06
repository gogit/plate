# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

from plate import create_app
from plate import start_service_server
from plate import start_test_server


def parse_argument():
    import optparse
    p = optparse.OptionParser('-m [test] or [run]')
    try:
        p.add_option('-m', dest='mode', type='string', default='run')
        options, args = p.parse_args()
        return options.mode
    except:
        print(p.get_usage())
        sys.exit()


def test_mode(config):
    app = create_app(config=config)
    from plate.watchdocs import APIDocumentObserver
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           doc_file_path_list=api_doc.toc['ORDER'])
    api_doc_observer.start_watch()
    start_test_server(app=app, port=app.config['PORT'])


def service_mode(config):
    app = create_app(config=config)
    from plate.watchdocs import APIDocumentObserver
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           doc_file_path_list=api_doc.toc['ORDER'])

    api_doc_observer.start_watch()
    start_service_server(app=app, port=app.config['PORT'])


if __name__ == '__main__':
    m = parse_argument()

    from plate.common.config import Config
    config = Config.load_conf('./config.json')

    # create documents
    from plate.api_document import APIDocument
    api_doc = APIDocument(config)

    if m == 'test':
        test_mode(config=config)
    elif m == 'run':
        service_mode(config=config)
    else:
        raise Exception("Not valid mode")
