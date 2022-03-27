instagram_data = {
    400001 : {
        "name":"punit",
        "followers":300,
        "reels":0,
        "post":15,
        "likes":100
    },
    400002:{
        "name":"gulzar",
        "followers":900,
        "reels":100,
        "post":50,
        "likes":300
    },
    400003:{
        "name":"tapas",
        "followers":500,
        "reels":200,
        "post":10,
        "likes":100
    },
    400004:{
        "name":"sameer",
        "followers":200,
        "reels":0,
        "post":10,
        "likes":400
    }

}

# print(instagram_data)

# print(instagram_data[400001]['followers'])

# print(instagram_data[400002]['post'])
# print(instagram_data[400004]['likes'])

instagram_data[400001].update({'hobbies':['cricket','cooking','travelling']})
print(instagram_data[400001])