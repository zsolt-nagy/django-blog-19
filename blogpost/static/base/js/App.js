function App(props) {
    const blogposts = ['First', 'Second', 'Third'];
    const blogpostsJsx = blogposts.map(
        post => <Blogpost title={post} key={post} />
    );
    return (
        <React.Fragment>
            <h2>{props.title}</h2>
            <ul>
                {blogpostsJsx}
            </ul>
        </React.Fragment>
    );
}

ReactDOM.render(
    <App title="App Component" />, 
    document.querySelector('.js-app-container')
);