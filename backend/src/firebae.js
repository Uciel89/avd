require('dotenv').config()

const {initializeApp, applicationDefault} = require('firebase-admin/app')

initializeApp({
    credential: applicationDefault()
})