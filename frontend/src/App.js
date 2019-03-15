import React, { Component } from 'react';
import { Form, InputGroup, Input, Alert } from 'reactstrap';
import Header from './Header/Header';
import Stories from './Stories/Stories';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      next: null,
      previous: null,
      loading: true,
      error: false,
      stories: [],
      searchValue: '',
    }
  }
  componentDidMount(){
    this.getStories('http://localhost:8000/stories/')
  }

  getStories = (url) => {
    this.setState({loading: true})
    fetch(url)
    .then(results => {
      return results.json();
    }).then(data => {
        this.setState({
          stories: data.results, 
          next: data.next, 
          previous: data.previous,
          loading: false,
          error: false
        })
    }).catch(error => {
      console.log(error);
      this.setState({ error: true, loading: false });
    });
  }

  updateInputValue = (evt) => {
    this.setState({
      searchValue: evt.target.value
    });
  }

  search = (search) =>{
    if(search){
      this.getStories('http://localhost:8000/stories/search/?q=' + search)
    } else {
      this.getStories('http://localhost:8000/stories/')
      this.setState({ searchValue: ''})
    }
  }

  render() {
    const {stories, next, previous, loading, error, searchValue} = this.state;
    return (
        <div className="App container-fluid p-0">
          <Header />
          <Form className="container mb-3" onSubmit={e => { e.preventDefault(); }}>
            <InputGroup>
              <Input type="text" name="search" id="Search" placeholder="Search" value={searchValue} onChange={this.updateInputValue}/>
              <button className='input-group-append btn btn-primary' onClick={() => {this.search(searchValue)}}>Search</button>
            </InputGroup>
          </Form>
          <Stories storyList={stories}/>
          <div className="container clearfix mt-3 mb-3">
            {previous !== null ? <button className="btn btn-secondary float-left" onClick={() => {this.getStories(previous)}}>Previous</button> : ''}
            {next !== null ? <button className="btn btn-primary float-right" onClick={() => {this.getStories(next)}}>Next</button> : ''}
          </div>  
          {loading ? 
            <div className="loader-backdrop">
              <div className="loader"></div>
            </div> : ''}
          {error ? 
            <Alert className="container" color="danger">
              Something went wrong please contact site administrator!
            </Alert>: ''}
        </div>
    );
  }
}

export default App;
