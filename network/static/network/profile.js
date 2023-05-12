document.addEventListener('DOMContentLoaded', function() {
    followers_number();
    user_posts(); 

    var elementExist = document.querySelector('#follow-button');
    console.log(elementExist);
    if (elementExist != null) {button_name()};
    document.querySelector('#follow-button').addEventListener('click', follow_unfollow)
})

function followers_number() {
    let user_id = document.querySelector('#followers-count').dataset.value;
    fetch(`/follow/count/${user_id}`)
    .then(response => response.json())
    .then(result => {
        // console.log(result.following_number);
        document.querySelector('#followers-count').innerHTML = `${result.followers_number} followers  ${result.following_number} following`;
    })
}

function  user_posts() {
    let user_id = document.querySelector('#followers-count').dataset.value;
    fetch(`/post/${user_id}`)
    .then(response => response.json())
    .then(posts => {
        posts.forEach(post => {
            console.log(post);
            let element = document.createElement('div')
            element.style.border = "dashed";
            element.innerHTML = `${post.content}<br>${post.timestamp}<br>${post.like} like(likes)<br>`;
            document.querySelector('#user-post-view').append(element);
        })

    })
}

function button_name() {
    let user_id = document.querySelector('#followers-count').dataset.value;

    fetch(`/follow/check/${user_id}`)
    .then(response => response.json())
    .then(result => {
        console.log(result.test)
        if (result.test == true) {
            document.querySelector('#follow-button').innerHTML = 'Unfollow';
        } else {
            document.querySelector('#follow-button').innerHTML = 'Follow';
        }
    })
}

function follow_unfollow() {

    let user_id = document.querySelector('#followers-count').dataset.value;

    if (document.querySelector('#follow-button').innerHTML == 'Follow') {
        fetch(`/follow/${user_id}`)
        .then(response => response.json())
        .then(result => {
            console.log(result.message);
            document.querySelector('#follow-button').innerHTML = 'Unfollow';
        })
    } else {
        fetch(`/unfollow/${user_id}`)
            .then(response => response.json())
            .then(result => {
                console.log(result.message);
                document.querySelector('#follow-button').innerHTML = "Follow";
            })
    }
}