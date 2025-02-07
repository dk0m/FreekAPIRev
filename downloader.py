import requests, base64

# freek.to segment downloader 


# clips are not necessarily a fixed number of seconds (2 - 10+) i think.
# clipId's format is seg-{clipNumber}-v1-a1.{format}, format (css, webp, png) changes to make it hard for reversers to understand the logic behind the API, it could be really anything and is not restricted to video formats.
# formats found: (webp, css, png, js), it could be anything at this point.

# IMPORTANT: formats dont matter, they wont really change anything, they are a form of obfuscation.
# you MUST send in a format, although it may be useless information to the server, it will still need a format to work.

# you cant send ambigious data after the (.), a format like css, js or png will work fine.

headers = {
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    'Referer': 'https://embed.su/',
    'Origin': 'https://embed.su/'
}

# the v1-a1 part changes depending on what quality/version of the show you're watching.
clipFormat = 'seg-{}-v1-a1.{}'

segsServer = f'https://viper.congacdn.cc/tralvonstone89.online/file2'
segsToDownload = 100

# this is an identifier for the movie whose clips you're trying to find, This is the identifier for the show 'Mr Robot', I fetched this while reversing the API, Other services may use a similar system like this.
meta = 'ivCI0wqyeyTdD9cMS21csdfXc4sowJX3UiovL5jaF5dCx8hW0FpyAcdwhQuhJAQUKRttJw7EGNgQPVaonZ2MMdwjtoTFKDRDq5HCHFACcxdqf6cMzq1gqkHhUJzYcCsk+MKA2UFU9G4iHbG1yg98RCXRhNFI1f6qwgNix~yDREk=/MTA4MA=='

for i in range(segsToDownload):
    clipId = base64.b64encode(clipFormat.format(i, 'js').encode()).decode() # seg-{clipNumber}-v1-a1.{format} (base64'd)
    req = requests.get(f'{segsServer}/{meta}/{clipId}', headers = headers)

    # some segments may not even exist, so we need to check the size of the segment if its lower than or equal to 512 bytes then its definitely not valid.
    if len(req.content) <= 512:
        continue
    
    if req.status_code != 200:
        continue

    with open(f'{i}thseg.mp4', 'wb') as segment:
        segment.write(req.content)
        segment.close()
        
        segSize = (len(req.content) / 1000) / 1024

        print(f'Downloaded {i}th Segment, Size: {segSize:.2f} MB!')
