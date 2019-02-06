from django.http import Http404
from django.utils.html import strip_tags
XML_MIMETYPES = (
    'application/xml',
    'text/xml',
)

HTML_MIMETYPES = (
    'text/html',
    'application/xhtml+xml'
)

def serve_pdf_galley_to_browser(request, file, article):
    """
    Serves a file to the browser so that it displays in the browser.
    :param request: HttpRequest object
    :param file: File object
    :param article: Article object
    :return: HttpResponse
    """
    file_path = os.path.join(
        settings.BASE_DIR,
        'files',
        'articles',
        str(article.id),
        str(file.uuid_filename)
    )

    try:
        response = HttpResponse(
            FileWrapper(open(file_path, 'rb')),
            content_type=file.mime_type
        )
        return response
    except IOError:
        messages.add_message(request, messages.ERROR, 'File not found.')
        raise Http404

