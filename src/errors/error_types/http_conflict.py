class HttpConflictError(Exception):
  def __init__(self, message: str) -> None:
    super().__init__(message)
    self.message = message
    self.name = "Conflicts"
    self.status_code = 409