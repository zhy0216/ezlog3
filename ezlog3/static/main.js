
Zepto(function($){
    console.log("ready!");

    $("#tweet-textarea").on("keydown", function(e){
        if(e.ctrlKey && e.which === 13){
            var $textarea = $("#tweet-textarea");
            var content = $textarea.val()
            if(content !== ""){
                $.post("/api/tweet/",{
                    "content": content
                }, function(data){
                    console.log(data)
                    if(data.rcode === 200){
                        $textarea.val("");
                        $("#tweet-container").prepend(data.tweet)
                    }
                })
            }
        }
    })

})


