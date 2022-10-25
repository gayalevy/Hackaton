import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCILZatEnOtF9nPwVptqjQNiIJ-GxIY0JA",
  'authDomain': "donationnotebool-85fad.firebaseapp.com",
  'projectId': "donationnotebool-85fad",
  'storageBucket': "donationnotebool-85fad.appspot.com",
  'messagingSenderId': "542348155908",
  'appId': "1:542348155908:web:db09f2fe9676435a04e951",
  'measurementId': "G-4Y1Z7MB54G"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


# Push Data
def main():
    data = {"name": "John", "age": 20, "address": ["new york", "Los Angeles"]}
    db.push(data)


# def main():


if __name__ == '__main__':
    main()
