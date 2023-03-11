# Week 3 — Decentralized Authentication

## AWS Cognito
### Creating a user pool


#### Summary
![Cruddr User Pool](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-user-pool1.png)
![Cruddr User Pool](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-user-pool2.png)


### Installing AWS Amplify Library
```sh
cd frontend-react-js
npm i aws-amplify --save
```
### Configuring Amplify
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/661314df2571e75eb97f3bcd954ad94c4d484ad4)

```js
import { Amplify } from 'aws-amplify';

Amplify.configure({
  "AWS_PROJECT_REGION": process.env.REACT_AWS_PROJECT_REGION,
  "aws_cognito_identity_pool_id": process.env.REACT_APP_AWS_COGNITO_IDENTITY_POOL_ID,
  "aws_cognito_region": process.env.REACT_APP_AWS_COGNITO_REGION,
  "aws_user_pools_id": process.env.REACT_APP_AWS_USER_POOLS_ID,
  "aws_user_pools_web_client_id": process.env.REACT_APP_CLIENT_ID,
  "oauth": {},
  Auth: {
    // We are not using an Identity Pool
    // identityPoolId: process.env.REACT_APP_IDENTITY_POOL_ID, // REQUIRED - Amazon Cognito Identity Pool ID
    region: process.env.REACT_AWS_PROJECT_REGION,           // REQUIRED - Amazon Cognito Region
    userPoolId: process.env.REACT_APP_AWS_USER_POOLS_ID,         // OPTIONAL - Amazon Cognito User Pool ID
    userPoolWebClientId: process.env.REACT_APP_AWS_USER_POOLS_WEB_CLIENT_ID,   // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
  }
});
```

#### Adding Variables to docker-compose.yml

```yml
      REACT_AWS_PROJECT_REGION: "${AWS_DEFAULT_REGION}"
      REACT_APP_AWS_COGNITO_REGION: "us-east-1"
      REACT_APP_AWS_USER_POOLS_ID: "us-east-1_FmG3hQ4EX"
      REACT_APP_CLIENT_ID: "10e2n8q6s6ns9qkq5ieju289ig"
```
##### REACT_APP_AWS_USER_POOLS_ID
<img width="1078" alt="App Client ID" src="https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-user-pool1.png">

##### REACT_APP_CLIENT_ID
<img width="1078" alt="App Client ID" src="https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-user-pool2.png">

## Impolement Amplify in HomeFeed page

[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/89f41bf42923e7d38303d7dd1adad869782b9b24)

In `HomeFeedPage.js`:
```js
//Add this to the import block
import { Auth } from 'aws-amplify';

//replace existing checkAuth function with the following function
const checkAuth = async () => {
  Auth.currentAuthenticatedUser({
    // Optional, By default is false. 
    // If set to true, this call will send a 
    // request to Cognito to get the latest user data
    bypassCache: false 
  })
  .then((user) => {
    console.log('user',user);
    return Auth.currentAuthenticatedUser()
  }).then((cognito_user) => {
      setUser({
        display_name: cognito_user.attributes.name,
        handle: cognito_user.attributes.preferred_username
      })
  })
  .catch((err) => console.log(err));
};
```




## Sign-in Page

[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/89f41bf42923e7d38303d7dd1adad869782b9b24)

in `SigninPage.js`:

```js
import { Auth } from 'aws-amplify';

const onsubmit = async (event) => {
  setErrors('')
  event.preventDefault();
  Auth.signIn(email, password)
  .then(user => {
    localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken)
    window.location.href = "/"
  })
  .catch(error => {
    if (error.code == 'UserNotConfirmedException') {
      window.location.href = "/confirm"
    }
    setErrors(error.message)
  });
  return false
}
```

In `ProfileInfo.js`:
```
//Add this to the import block
import { Auth } from 'aws-amplify';

//replace existing signOut function with the following function
  const signOut = async () => {
    try {
        await Auth.signOut({ global: true });
        window.location.href = "/"
    } catch (error) {
        console.log('error signing out: ', error);
    }
  }
```

## Sign up Page

`SignupPage.js`

```js
const onsubmit = async (event) => {
  event.preventDefault();
  setErrors('');
  console.log('username', username);
  console.log('email', email);
  console.log('name', name);
  try {
    const { user } = await Auth.signUp({
      username: email,
      password: password,
      attributes: {
        name: name,
        email: email,
        preferred_username: username,
      },
      autoSignIn: {
        enabled: true,
      },
    });
    console.log(user);
    window.location.href = `/confirm?email=${email}`;
  } catch (error) {
    console.log(error);
    setErrors(error.message);
  }
  return false;
};
```

## Confirmation Page

`ConfirmationPage.js`

```js
const resend_code = async (event) => {
  setErrors('');
  try {
    await Auth.resendSignUp(email);
    console.log('Code resent successfully');
    setCodeSent(true);
  } catch (err) {
    console.log(err);
    if (err.message === 'Username cannot be empty') {
      setErrors('You need to provide an email in order to send Resend Activation Code.');
    } else if (err.message === 'Username/client id combination not found.') {
      setErrors('Email is invalid or cannot be found.');
    }
  }
};
```


## Creating a user in Cognito
<img width="815" alt="Create User in AWS Cognito" src="https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-create-user.png">

Manually verifying the user
```sh
aws cognito-idp admin-set-user-password --username fafbc35a-08cc-4af5-8d9b-2ca35a0d2f4f --password REDACTED --permanent --user-pool-id us-east-1_FmG3hQ4EX
```

##Confirm User
<img width="815" alt="Confirmed user in AWS Cognito" src="https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-confirmed-user.png">



## Adding Optional Attributes in Cognito
![Cognito User- Optional Attributes](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-user-optional.png)

### Verification
![Verification](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cruddur-user-attributes.png)


## Password Recovery Page

[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/f469148db5d6e7db7bacb6642e76a5fcf386a6ed)

`RecoverPage.js`
```js
const onsubmit_send_code = async (event) => {
  event.preventDefault();
  setErrors('');
  Auth.forgotPassword(username)
    .then((data) => setFormState('confirm_code'))
    .catch((err) => setErrors(err.message));
  return false;
};
```



```js
const onsubmit_confirm_code = async (event) => {
  event.preventDefault();
  setErrors('');
  if (password === passwordAgain) {
    Auth.forgotPasswordSubmit(username, code, password)
      .then((data) => setFormState('success'))
      .catch((err) => setErrors(err.message));
  } else {
    setErrors('Passwords do not match');
  }
  return false;
};
```  


## Passing the JWT token along to the backend
When configuring authentication for storage we have added the following line to `SigninPage.js`:
```js
localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken)
```


### Updating the Backend

[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/fef8c80096dc9b463ffcf56d185cb886bf89220d)

To pass the JWT to backend, in `HomeFeedPage.js` we are updating the `const res` with Authorization header:
```js
const res = await fetch(backend_url, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
```

In `app.py`:

- Adding CORS config
```py
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  headers=['Content-Type', 'Authorization'], 
  expose_headers='Authorization',
  methods="OPTIONS,GET,HEAD,POST"
)
```

- Adding the header read to the flask backend:

```py
@app.route("/api/activities/home", methods=['GET'])
def data_home():
  app.logger.info("AUTH HEADER")
  app.logger.info(request.headers.get('Authorization'))
  data = HomeActivities.run(Logger = LOGGER)
  return data, 200
```

#### Verification

```yml
192.168.40.10 - - [11/Mar/2023 12:39:21] "OPTIONS /api/activities/home HTTP/1.1" 200 -
authenticated
{'sub': '90c28f33-f898-435e-a11d-b47b9634946a', 'iss': 'https://cognito-idp.us-east-1.amazonaws.com/us-east-1_FmG3hQ4EX', 'client_id': '10e2n8q6s6ns9qkq5ieju289ig', 'origin_jti': '30a03a42-8f8d-4305-aaae-6783d3696ab6', 'event_id': '4fd8a4d5-c14f-415c-a67c-104643560ac9', 'token_use': 'access', 'scope': 'aws.cognito.signin.user.admin', 'auth_time': 1678538359, 'exp': 1678541959, 'iat': 1678538359, 'jti': '9abe83f5-971e-4a2b-a372-a1edeadec84c', 'username': '90c28f33-f898-435e-a11d-b47b9634946a'}
90c28f33-f898-435e-a11d-b47b9634946a
 ```
<img width="815" alt="JWT token in AWS Cognito" src="https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/jwt-cognito.png">

### Token Validation
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/github.com/nickda/aws-bootcamp-cruddur-2023/commit/8413adf8e928f06c5c45e92cecabc977078b209a)

<img width="815" alt="JWT token in AWS Cognito" src="https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/c22b1dbc9bc83b2e8443422cc1794d9c26d5f8c3/_docs/assets/week3/cognito-authenticated.png">

#### Installing Flask-AWSCognito
```sh
pip3 install -r requirements.txt
```
#### Adding EnvVars to docker compose
 ```yml
      AWS_COGNITO_USER_POOL_ID: "us-east-1_FmG3hQ4EX"
      AWS_COGNITO_USER_POOL_CLIENT_ID: "10e2n8q6s6ns9qkq5ieju289ig"
 ```

#### Code for Cognito Token Verification
refer to the [commit](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/f007218891160833a052a9c9e39eb820683bf8f1)


#### Configuring Cognito in app.py
refer to the [commit](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/f007218891160833a052a9c9e39eb820683bf8f1)

 
#### Updating the home_activities.py
refer to the [commit](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/f007218891160833a052a9c9e39eb820683bf8f1) 

## Dynamic CSS Theming with variables
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/68b653901fafc4b44a8937d1ce7f7bc913afdacc)
