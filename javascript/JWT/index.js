const express = require("express");
const app = express();
const mongoose = require("mongoose");
const bodyParser = require("body-parser");

dotenv = require("dotenv");
dotenv.config();


mongoose.connect("mongodb+srv://sudip:MongoDB123@cluster0.iwq7e3d.mongodb.net/jwt",{
    useNewUrlParser: true,
   
})
.then(()=>{
    console.log("connected to database")
}
)
.catch((error)=>{
    console.log("error connecting to database", error)
    process.exit(1)

}
);
app.use(bodyParser.json());
app.listen(3000,()=>{
    console.log("server is running on port 3000")
}
);
app.use("/api", require("./routes/user"));
