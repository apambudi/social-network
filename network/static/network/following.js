document.addEventListener('DOMContentLoaded', function() {
    load_posts();
})

function load_posts() {
    fetch('/follow-post')
    .then(response => response.json())
    .then(posts =>  {
        posts.forEach(post => {
            console.log(post);
            let element = document.createElement('div');
            element.style.border = "dotted";
            element.innerHTML = `<a href="/profile/${post.user_id}">${post.username}</a><br>${post.content}<br>${post.timestamp}<br>${post.like} like(likes)<br>`;
            document.querySelector('#post-view').append(element);
        }
        );
    })
}