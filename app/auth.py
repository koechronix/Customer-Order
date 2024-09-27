from flask import redirect, url_for, session, flash
from authlib.integrations.flask_client import OAuth
from . import app

# Set up OAuth/OpenID Connect
oauth = OAuth(app)
oidc = oauth.register(
    'oidc',
    client_id=app.config['OIDC_CLIENT_ID'],
    client_secret=app.config['OIDC_CLIENT_SECRET'],
    authorize_url=app.config['OIDC_AUTHORIZATION_URL'],
    token_url=app.config['OIDC_TOKEN_URL'],
    userinfo_endpoint=app.config['OIDC_USERINFO_URL'],
    client_kwargs={'scope': 'openid email profile'}
)

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oidc.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    try:
        token = oidc.authorize_access_token()
        user_info = oidc.parse_id_token(token)
        session['user'] = user_info
        return f"Hello, {user_info['name']}"
    except Exception as e:
        return f"Authentication failed: {str(e)}", 400

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))  # Redirect to home or login page
