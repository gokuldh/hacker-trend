import React, { Component } from 'react';
import { ListGroup, ListGroupItem, ListGroupItemHeading, ListGroupItemText } from 'reactstrap';

class Stories extends Component {
  render() {
    const { storyList } = this.props;
    const list = storyList.length > 0 ? storyList.map((item, i) => {
      return (
          <ListGroupItem key={i} index={i}>
            <ListGroupItemHeading>{item.title} {item.url ? <a href={item.url}>({item.url})</a> : ''}</ListGroupItemHeading>
            <ListGroupItemText className="m-0">
              <span>{item.score} points by {item.username} </span> 
            </ListGroupItemText>
            <ListGroupItemText className={item.sentiment}>
              Sentiment: {item.sentiment}
            </ListGroupItemText>
          </ListGroupItem>
        );
    }) : null;

    return (
      <div className="container">
      
      <ListGroup >
          {list ? list : 
          <ListGroupItem>
            <ListGroupItemHeading>No Results Found!</ListGroupItemHeading>
          </ListGroupItem>
        }
        </ListGroup>
      </div>
    );
  }
}

export default Stories;