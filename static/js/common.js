$(function () {

    console.log("loading success")
    var now = new Date()
    sessionid = now.getTime()
    if (checkCookie()){
        console.log("already exists")
    }else {
        setCookie("loginsession",sessionid,7)
    }

    function setCookie(cname,cvalue,exdays) {

        var d = new Date();
        d.setTime(d.getTime()+(exdays*24*60*60*1000));
        var expires = "expires="+d.toUTCString();
        document.cookie = cname+'='+cvalue+';'+expires;
         console.log("set success")
    }

    function getCookie(cname) {

        var name = cname+"=";
        var cookiearry = document.cookie.split(';')
        for (var i=0;i<cookiearry.length;i++){

            var c = cookiearry[i].trim()
            if ( c.indexOf(cname)==0){

                return c.substring(name.length,c.length)
            }
        }
        return ""
    }

    function checkCookie() {

        var user = getCookie("loginsession");
        if (user!=""){

            return true
        }else {

            return false
        }
    }
})