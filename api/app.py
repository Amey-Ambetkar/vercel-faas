def handler(request):
    return {
        "statusCode": 200,
        "body": "Hello from Vercel Serverless Function!",
        "headers": {
            "Content-Type": "text/plain"
        }
    }
