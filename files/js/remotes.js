function show_remote(name) {
    $(".remoteContol").hide();
    $("#" + name).show();
}

function send_once(name, key) {
    $.post(backend + "/send_once", "remote=" + name + "&key=" + key);
}

function send_start(name, key) {
    if (pressed) {
        $.post(backend + "/send_start", "remote=" + name + "&key=" + key);
    }
}

function send_stop(name, key) {
    $.post(backend + "/send_stop", "remote=" + name + "&key=" + key);
}

var pressed = false;
$(".click").on('touchstart mousedown', function(e) {
    remote = $(this).parent().attr("id");
    key = $(this).attr('id');
    e.preventDefault();
    send_once(remote, key);
    
    pressed = true;
    setTimeout(send_start, 500, remote, key);
});

$(".click").on('touchend mouseup', function(e) {
    remote = $(this).parent().attr("id");
    key = $(this).attr('id');
    
    e.preventDefault();
    if (pressed) {                    
        send_stop(remote, key);
    }
    pressed = false;
});