import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

const firebaseConfig = {
    apiKey: "AIzaSyCwgIXLZjlOkXkYg70aQYpzpuFAxsHOVR8",
    authDomain: "portfolio-2803.firebaseapp.com",
    projectId: "portfolio-2803",
    storageBucket: "portfolio-2803.firebasestorage.app",
    messagingSenderId: "786579821498",
    appId: "1:786579821498:web:0ea9eef85f05f49e3e4383",
    // measurementId: "G-Q7L1FV84YB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);