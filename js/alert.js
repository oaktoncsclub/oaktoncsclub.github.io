$(document).ready(function() {
    $.notify({
        icon: "glyphicon glyphicon-bullhorn",
        title: "",
        message: 'We will <strong>NOT</strong> have a meeting on <time datetime="2016-10-19">Wednesday Oct. 19</time> because it\'s PSAT day'
    }, {
        type: "danger",
        delay: 0,
        template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
            '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
            '<div>' +
            '<span data-notify="icon"></span> ' +
            '<strong data-notify="title">{1}</strong> ' +
            '</div>' +
            '<span data-notify="message">{2}</span>' +
            '<div class="progress" data-notify="progressbar">' +
            '<div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div>' +
            '</div>' +
            '<a href="{3}" target="{4}" data-notify="url"></a>' +
            '</div>'
    });
})
