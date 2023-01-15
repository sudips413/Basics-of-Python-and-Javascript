const express = require("express");
const router = express.Router();
const {TOKEN_KEY} = process.env;


const User = require("../model/user");
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");

router.post('/register', async (req, res) => {
    try{
        const {first_name, last_name, email, password} = req.body;
        if(!(email && password && first_name && last_name)){
            res.status(400).json({
                message: "All input is required",
                success: false,
            })
        }
        const oldUser = await User.findOne({email});
        if(oldUser){
            return res.status(409).json({
                message: "User already exists. Please Login",
                success: false
        }
        );
        }
        //Encrypt user password
        encryptedPassword = await bcrypt.hash(password,10)
        //Create user in our database
        const user = await User.create({
            first_name,
            last_name,
            email: email.toLowerCase(),
            password: encryptedPassword,
        });
        //Create token
        const token = jwt.sign(

            {user_id : user._id,email},
            TOKEN_KEY,{
                expiresIn:"2h",
            }            

        );
        user.token = token;
        // //Save user
        // await user.save();
        //Return new user
        res.status(201).json({
            message: "User created successfully",
            success: true,
            data:user,
        });

    }
    catch(error){
        console.log(error);
    }
}
);
router.post("/login", async (req, res) => {
    try{
        console.log(req.body);
        const{email,password}=req.body;
        console.log(email)
        if(!(email && password)){
            res.status(400).json({
                message: "All input is required",
                success: false,
            })
        }
        const user = await User.findOne({email});
        if(user &&(await bcrypt.compare(password, user.password))){
            const token = jwt.sign(
                {user_id: user._id, email},
                TOKEN_KEY,
                {
                    expiresIn: "2h",
                }
            );
            user.token=token;
            res.status(200).json({
                message: "User logged in successfully",
                success: true,
                data:user,
            });
        }

    }
    catch(error){
        console.log(error);
    }
});

module.exports = router;