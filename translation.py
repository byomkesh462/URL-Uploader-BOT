class Translation(object):
    START_TEXT = """Hello! 🙋

This is A Powerful Url Uploader Bot that Supports many sites based on YTDLp. 

This Bot can Upload in File and Video Format to Telegram with Permanent Thumbnail Support. 

/help To know how to use me !

Developed with ❤ 
"""

    HELP_USER = """It's not complicated to use me! 😅
    
✪ Send Image As permanent Thumbnail (Optional).

✪ Send url (example.com/filename.mp4 | New Filename.mp4).

✪ Press /deletethumbnail to delete the current thumbnail.

✪ Select the button:
   Video  - streamable video without screenshot
   SVideo - streamable video with screenshot
   File  - Doc file without screenshot
   DFile  - Doc file with screenshot
   
<b>✪ NB</b> : It is recommended to use a custom thumbnail because sometimes it won't upload the file without a custom thumbnail."""
    ABOUT_TEXT = """<b>🤖 My Name:</b> URL Upload Bot.

<b>👨‍💻 Developer:</b> <a href='https://t.me/m8u3_bot'>m3u8</a>

<b>📝 Language:</b> Python 3

<b>📕 Library:</b> Pyrogram 1.0.7

<b>🔔 Updates Channel:</b> <a href='https://t.me/ullastv'>ULLASTV</a>"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate.</a> \n\nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\n\nYou can use /deletethumbnail to delete the auto-generated thumbnail.\n"
    SET_CUSTOM_USERNAME_PASSWORD = """\n If you want to download premium videos, provide the following format:\n
URL | filename | username | password"""
    DOWNLOAD_START = "📥 Downloading to my server..."
    UPLOAD_START = "📤 Uploading to telegram..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected file size {}\n\nSorry. But I cannot upload files greater than 2GB due to Telegram API limitation."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using the bot.\n\n<b>Join:</b> @ULLASTV"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds."
    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This image will be used in the next videos/files."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared successfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled successfully."
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
