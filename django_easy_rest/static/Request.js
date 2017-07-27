function RequestHandler(url) {

    this.url = url;
    /**
     * on failure returns {"error":"error value"}
     * @return {object}
     */
    this.SendSync = function (data) {
        let ajax_response = undefined;
        let dataToSend = JSON.stringify(data);
        $.ajax(
            {
                async: false,
                url: this.url,
                type: 'POST',
                data: dataToSend,
                headers: {"X-CSRFToken": getCsrf()},

                success: function (jsonResponse) {
                    ajax_response = JSON.parse(jsonResponse);


                },
                error: function (error) {
                    ajax_response = {"error": error}

                }
            });
        return ajax_response;

    };

    this.SendAsync = function (data, OnSuccess, OnError = function (error) {
    }) {
        let dataToSend = JSON.stringify(data);
        $.ajax(
            {
                async: true,
                url: this.url,
                type: 'POST',
                data: dataToSend,
                headers: {"X-CSRFToken": getCsrf()},

                success: OnSuccess,
                error: OnError
            });

    };
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getCsrf() {
    return getCookie("csrftoken")
}