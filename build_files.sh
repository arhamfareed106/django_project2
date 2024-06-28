{
  "version": 2,
  "builds": [
    {
      "src": "project/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtimes":"Python 3.12.2" }
    }

    {
        "src": "build_files.sh",
        "use": "@vercel/static_build"
        "config":{
        
        }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "manage.py"
    }
  ]
}
