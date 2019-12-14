import importing

# The imported functions are stored in dir(importing)
# This is where the "on_" prefix comes in handy
for obj in dir(importing):
    if "on_" in obj:
        method = getattr(importing, obj)
        method()