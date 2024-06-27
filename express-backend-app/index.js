const express = require('express')
const app = express()
const port = 3000

app.get('/', function(req, res) {
  res.send('Hello World!')
})

app.get('/route1',function(req,res){
    res.send('Hello from route1')
})

app.get('/route2',function(req,res){
    res.send('Hello from route2')
})

app.listen(port, function()  {
  console.log(`Example app listening on port ${port}`)
})