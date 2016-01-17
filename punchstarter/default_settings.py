import os
import cloudinary

DEBUG=os.environ.get("DEBUG", True)
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI","sqlite:///"+ BASE_DIR + "/app.db")
CLOUDINARY_CLOUD_NAME=os.environ.get("CLOUDINARY_CLOUD_NAME", "dijdhlar0")
CLOUDINARY_API_KEY=os.environ.get("CLOUDINARY_API_KEY", "699454286215986")
CLOUDINARY_API_SECRET=os.environ.get("CLOUDINARY_API_SECRET", "EFu2EmBiXqWxgXts6NWuR4Y7sWo")

cloudinary.config( 
  cloud_name = CLOUDINARY_CLOUD_NAME, 
  api_key = CLOUDINARY_API_KEY, 
  api_secret = CLOUDINARY_API_SECRET" 
)


