kvStore = function (key, value, callback, err) {
        //send ajax request
        jQuery.ajax({
            type: "POST",
            url: "../kvStore",
            data: {
                "key": key,
                "value": value,
            },
            success: function (data) {
                console.log("got data", data)
                if (callback) callback(data)
            },
            error: function (error) {
                console.log("error", error)
                if (err) err()

            }
        });
    }

    kvGet = function (key, callback, err) {
        //send ajax request
        jQuery.ajax({
            type: "POST",
            url: "../kvGet",
            data: {
                "key": key,
            },
            success: function (data) {
                console.log("got data", data)
                if (callback) callback(data)
            },
            error: function (error) {
                console.log("error", error)
                if (err) err()
            }
        });
    }

    kvDelete = function (key, callback, err) {
        //send ajax request
        jQuery.ajax({
            type: "POST",
            url: "../kvDelete",
            data: {
                "key": key,
            },
            success: function (data) {
                console.log("got data", data)
                if (callback) callback(data)
            },
            error: function (error) {
                console.log("error", error)
                if (err) err()
            }
        });
    }

    kvList = function (prefix, callback) {
        //send ajax request
        jQuery.ajax({
            type: "POST",
            url: "../kvList",
            data: {
                "prefix": prefix,
            },
            success: function (data) {
                console.log("got data", data)
                if (callback) callback(data)
            },
            error: function (error) {
                console.log("error", error)
            }
        });
    }
