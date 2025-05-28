import boto3
from PIL import Image
import io
import base64
import json

def lambda_handler(event, context):
    # Decode the image from the request
    try:
        body = json.loads(event['body'])
        image_data = base64.b64decode(body['image'])
        resize_width = int(body.get('width', 300))
        resize_height = int(body.get('height', 300))
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid request: ' + str(e)})
        }

    try:
        # Open the image
        image = Image.open(io.BytesIO(image_data))

        # Resize the image
        resized_image = image.resize((resize_width, resize_height))

        # Convert the image back to bytes
        buffer = io.BytesIO()
        resized_image.save(buffer, format=image.format)
        buffer.seek(0)

        # Encode the resized image to base64
        resized_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return {
            'statusCode': 200,
            'body': json.dumps({'resized_image': resized_base64}),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Image processing failed: ' + str(e)})
        }
