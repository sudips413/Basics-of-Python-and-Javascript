const jwt = require("jsonwebtoken");   
const {TOKEN_KEY} = process.env; 


const verifyToken = (req,res,next)=>{
    const token = req.body.token || req.query.token || req.headers["x-access-token"];
    if(!token){
        return res.status(403).json({
            message: "A token is required for authentication",
            success: false,

        });
    }
    try{
        console.log(token);
        const decoded = jwt.verify(token,TOKEN_KEY);
        req.user = decoded;
    }
    catch(error){
        return res.status(401).json({
            message:"Invalid token",
            success: false,
        });
    }
}
module.exports = verifyToken;
