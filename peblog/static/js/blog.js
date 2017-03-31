

function createXmlHttp() {
        var xmlHttp = null;
        try {
                xmlHttp = new XMLHttpRequest();
        } catch (e) {
                try {
                        xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
                } catch (e) {
                        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
                }
        }
        return xmlHttp;
}

function research(formId) {
        var xmlHttp = createXmlHttp();
        if(!xmlHttp) {
                alert("您的浏览器不支持AJAX！");
                return 0;
        }
        var F = document.getElementById(formId);

        var search = F.search.value;
        var e = document.getElementById(formId);
        var url = e.action;
        var getData = "search="+search;
        xmlHttp.open("GET", url, true);
        xmlHttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xmlHttp.send(getData);
        xmlHttp.onreadystatechange = function() {
                if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                        window.location.href="/blog/search/?search=" + search;
                    }
                }
}
