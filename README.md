# Adobe KMUTNB
Automated grant Adobe access for KMUTNB students

## How it works?
It's a simple request process.

## How to use?
1. Fork this project.
2. Create secrets in the repository secrets:
   - `KMUTNB_USERNAME=s6601234567890`
   - `KMUTNB_PASSWORD=your_password_here`

   2.1 If `payload.py` is not working, Remove the dotenv file code and edit the username and password directly in the payload file. Save the file, but be cautious not to publish your password publicly.
   
3. Add the GitHub Action workflow to the repository.
4. Done!
