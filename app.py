from flask import Flask, render_template, request, redirect, url_for, flash
from collections import deque

app = Flask(__name__)
app.secret_key = "4b3f4cd94cbbd8f0c0f03d76e453d2d4" 

# Example attendee list and credentials
attendee_list = ["John Doe", "Jane Smith", "Ahmed Al-Khaldi", "Alice Johnson"] 
credentials = deque([
    {"username": "sdeeu", "password": "aPCm"},
    {"username": "ycvft", "password": "nAEK"},
    {"username": "atzng", "password": "A3Ad"},
    {"username": "qpygf", "password": "NAgw"},
    {"username": "mznur", "password": "rz63"},
    {"username": "uvuam", "password": "2VFE"},
    {"username": "sweah", "password": "hevb"},
    {"username": "zdvyv", "password": "D@v8"},
    {"username": "ndqwa", "password": "3ck5"},
    {"username": "vtkky", "password": "P6A7"},
    {"username": "ahpfh", "password": "SgFZ"},
    {"username": "rfmxu", "password": "3nA6"},
    {"username": "ewpbe", "password": "q2zP"},
    {"username": "sbqmh", "password": "rTSE"},
    {"username": "uasrh", "password": "6m3r"},
    {"username": "hmfqf", "password": "CDXZ"},
    {"username": "bayde", "password": "Tcqa"},
    {"username": "kyzgb", "password": "qeQH"},
    {"username": "hscng", "password": "TVDC"},
    {"username": "kppwy", "password": "ef8p"},
    {"username": "zhwhq", "password": "yvzw"},
    {"username": "pdrae", "password": "3qcZ"},
    {"username": "pgbse", "password": "VgKE"},
    {"username": "buuma", "password": "Z3yY"},
    {"username": "urvfs", "password": "krkh"},
    {"username": "bcnke", "password": "pRvq"},
    {"username": "newhr", "password": "BkTW"},
    {"username": "szcdq", "password": "CxQ5"},
    {"username": "zdwrm", "password": "6yP3"},
    {"username": "etgne", "password": "3UsU"},
    {"username": "buyhs", "password": "8Vxb"},
    {"username": "dfvxr", "password": "A9B9"},
    {"username": "nnbcg", "password": "MdeP"},
    {"username": "ermnf", "password": "vEYR"},
    {"username": "emeak", "password": "6uze"},
    {"username": "vbvsc", "password": "DaBc"},
    {"username": "fwxsv", "password": "tcMM"},
    {"username": "hxrzc", "password": "tdDR"},
    {"username": "gfpxy", "password": "W78H"},
    {"username": "pkvcg", "password": "ECTv"},
    {"username": "wysxp", "password": "ccbe"},
    {"username": "aaxyq", "password": "tbqW"},
    {"username": "ygmhb", "password": "GyCW"},
    {"username": "pmrux", "password": "Pt8K"},
    {"username": "hgqhr", "password": "sFWg"},
    {"username": "eqaaa", "password": "DQUw"},
    {"username": "bavkf", "password": "6ZXZ"},
    {"username": "hfccm", "password": "S9rT"},
    {"username": "rxpkv", "password": "8deT"},
    {"username": "yxatq", "password": "gCfX"},
    {"username": "stxny", "password": "6BFx"},
    {"username": "utcdk", "password": "QCVb"},
    {"username": "yvuzr", "password": "9zDv"},
    {"username": "ccgxu", "password": "W4KP"},
    {"username": "dwygc", "password": "HYdz"},
    {"username": "wzngh", "password": "G6yW"},
    {"username": "tevbh", "password": "GnnT"},
    {"username": "emmcx", "password": "NAHQ"},
    {"username": "mxxba", "password": "qC64"},
    {"username": "hbfbq", "password": "N7Cg"},
    {"username": "adtxk", "password": "XgPU"},
    {"username": "hpszb", "password": "EKRG"},
    {"username": "akduy", "password": "7Wwc"},
    {"username": "hzczq", "password": "6aDt"},
    {"username": "dwshx", "password": "9T3K"},
    {"username": "crxpq", "password": "zXya"},
    {"username": "ftext", "password": "u5pf"},
    {"username": "ahqfd", "password": "u23P"},
    {"username": "cfybt", "password": "sp8k"},
    {"username": "tdhkg", "password": "Fs96"},
    {"username": "uvzap", "password": "tCtc"},
    {"username": "zqpzc", "password": "XdbD"},
    {"username": "pbcns", "password": "H9yC"},
    {"username": "qyudw", "password": "XyyD"},
    {"username": "ztgtu", "password": "a9KA"},
    {"username": "qdekg", "password": "43xW"},
    {"username": "gnsse", "password": "zdgQ"},
    {"username": "hekqw", "password": "dCmM"},
    {"username": "hxvvt", "password": "ayqC"},
    {"username": "qbfxc", "password": "8zFH"},
    {"username": "cqynv", "password": "Ve4Y"},
    {"username": "smbzz", "password": "ZmuT"},
    {"username": "skvgh", "password": "N3Qr"},
    {"username": "kbbaz", "password": "mdZZ"},
    {"username": "fvvum", "password": "PX5g"},
    {"username": "zuruc", "password": "r76H"},
    {"username": "ggsdu", "password": "wRK6"},
    {"username": "uyfrv", "password": "b5Y2"},
    {"username": "atccy", "password": "DAWD"},
    {"username": "wrtvz", "password": "N3yy"},
    {"username": "dkfxh", "password": "g3vu"},
    {"username": "ypzbz", "password": "qP8m"},
    {"username": "rgfmn", "password": "gVvW"},
    {"username": "xbkva", "password": "K8Tg"},
    {"username": "wuqea", "password": "mYTc"},
    {"username": "bpbxa", "password": "ASxu"},
    {"username": "wqdhz", "password": "mVzk"},
    {"username": "qkptg", "password": "NCa8"},
    {"username": "dseya", "password": "rFXW"},
    {"username": "eyutn", "password": "nXW5"}
])
# Track assigned credentials
assigned_credentials = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        attendee_name = request.form["name"].strip()

        if attendee_name not in attendee_list:
            flash("Attendee not found in the list.", "error")
            return redirect(url_for("index"))

        # Check if attendee already has credentials assigned
        if attendee_name in assigned_credentials:
            assigned_credential = assigned_credentials[attendee_name]
        else:
            if not credentials:
                flash("All credentials have been assigned.", "error")
                return redirect(url_for("index"))
            assigned_credential = credentials.popleft()
            assigned_credentials[attendee_name] = assigned_credential

        # Flash message with credentials
        flash(f"Assigned to {attendee_name} - Username: {assigned_credential['username']}, Password: {assigned_credential['password']}", "success")
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="148.151.47.31", port=5000)

