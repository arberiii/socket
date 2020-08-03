$(document).ready(function() {

    var socket = io.connect('http://127.0.0.1:5000');

    var socket_message = io("http://127.0.0.1:5000/messages");

    $('#send').on('click', function() {
        var message = $('#message').val();

        socket_message.emit('message from user', message);

    });

    socket.on('from flask', function(msg) {
        alert(msg);
    });

    socket.on('server originated', function(msg){
        alert(msg);
    })

    /*

    socket.on('connect', function() {
    
        socket.send('I am now connected!');

        socket.emit('custom event', {'name' : 'Anthony'});

        socket.on('from flask', function(msg) {
            alert(msg['extension']);
        });

        socket.on('message', function(msg) {
            alert(msg);
        });
        
    });

    */

});