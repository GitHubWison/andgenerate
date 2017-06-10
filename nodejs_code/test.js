var express = require('express');
var app = express();
app.get('/get_message',function (req,res) {
   res.end('12312312')
});
var server = app.listen(8081,function () {
    var host = server.address().address;
    var port = server.address().port;
    console.log("")
});
// console.log("hello")