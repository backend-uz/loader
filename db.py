import instaloader
import re
import os

loader = instaloader.Instaloader()
loader.login('akkforbot18', 'eski_parol')
session_file = 'session_file.txt'

if os.path.exists(os.path.join('.', session_file)):
    loader.load_session_from_file(username='akkforbot18', filename=session_file)
else:
    loader.save_session_to_file(filename=session_file)

def reel(url):
    shortcode = re.search(r"/reel/([A-Za-z0-9_-]+)/", url).group(1)
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    video_url = post.video_url
    return video_url


def slider(url):
    shortcode = re.search(r"/p/([A-Za-z0-9_-]+)/", url).group(1)
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
    try:
        urls = []
        for i in post.get_sidecar_nodes():
            if i.is_video:
                downloadable_url = i.video_url
            else:
                downloadable_url = i.display_url
            urls.append(downloadable_url)
        if urls:
            return urls

    except:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
    img_url = post.url
    return img_url


def getBasicInfo(url):
    profile = instaloader.Profile.from_username(loader.context, url)
    user_name = profile.username
    user_id = profile.userid
    posts = profile.mediacount
    followers = profile.followers
    followees = profile.followees
    bio = profile.biography
    ext_url = profile.external_url
    profile_pic = profile.profile_pic_url
    text = f"Username: {user_name}\nUser ID: {user_id}\nPosts: {posts}\nFollowers: {followers}\nFollowing Count: {followees}\nBio: {bio}\nExternal URL: {ext_url}"
    return [text, profile_pic]



