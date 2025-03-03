from src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HttpResponse:
  if isinstance(error, (HttpConflictError, HttpNotFoundError)):
    return HttpResponse (
      body={
        "erros":[
          {
            "title": error.name,
            "detaiils" : error.message
          }
        ]
      },
      status_code=error.status_code
    )
  
  return HttpResponse(
    body={
      "erros": [{
        "title" : "erro",
        "details": str(error)
      }]
    }
  )