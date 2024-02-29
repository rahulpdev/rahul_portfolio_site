
# TODO Select two sans serif fonts with similar moods and contrasting weights 5:15 from Humanist
# TODO Create Contact page
# TODO Create GitHub readme.md

"""
https://colorhunt.co/palette/6096b493bfcfbdcdd6eee9da
https://colorhunt.co/palette/364f6b3fc1c9f5f5f5fc5185
https://timmyomahony.com/
https://www.linkedin.com/in/rahulparmar/
https://github.com/rahulpdev
https://github.com/rahulpdev-homeassistant
https://twitter.com/rahulbrit/
https://asset.brandfetch.io/idNfPDHpG3/idCP5_ULRP.png
https://asset.brandfetch.io/idNfPDHpG3/idlcya_qWR.png
https://asset.brandfetch.io/idfWi_8mFJ/idztVEBpUb.svg
https://asset.brandfetch.io/ideyPcdlEj/idXFzgrst9.svg
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
