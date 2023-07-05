(function ($) {
    "use strict";

    $.fn.multiupload = function (options) {
        var settings = $.extend({
            url: '',
            fieldName: 'file',
            maxFileCount: 5,
            maxFileSize: 5,
            allowedExtensions: ['jpg', 'jpeg', 'png', 'gif'],
            success: function () {},
            error: function () {}
        }, options);

        return this.each(function () {
            var $element = $(this);
            var $fileInput = $('<input type="file" name="' + settings.fieldName + '[]" multiple>');
            var $submitButton = $('<button type="submit">Upload</button>');

            $element.append($fileInput).append($submitButton);

            $fileInput.on('change', function (e) {
                var files = e.target.files;

                if (files.length > settings.maxFileCount) {
                    alert('Maximum file count exceeded. Please select up to ' + settings.maxFileCount + ' files.');
                    return;
                }

                for (var i = 0; i < files.length; i++) {
                    var file = files[i];

                    if (file.size > settings.maxFileSize * 1024 * 1024) {
                        alert('File size exceeds the maximum limit of ' + settings.maxFileSize + 'MB.');
                        return;
                    }

                    var extension = file.name.split('.').pop().toLowerCase();
                    if ($.inArray(extension, settings.allowedExtensions) === -1) {
                        alert('Invalid file type. Only ' + settings.allowedExtensions.join(', ') + ' files are allowed.');
                        return;
                    }
                }

                var formData = new FormData();
                for (var j = 0; j < files.length; j++) {
                    formData.append(settings.fieldName + '[]', files[j]);
                }

                $.ajax({
                    url: settings.url,
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function (response) {
                        settings.success(response);
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        settings.error(jqXHR, textStatus, errorThrown);
                    }
                });
            });
        });
    };
}(jQuery));
