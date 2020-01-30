import React from 'react';

function Cell(props){
  const color = {
    1: 'black',
    2: 'white'
  }
  const style = {
    backgroundColor: '#92a8d1',
    border: '1px solid black',
    width: '50px',
    height: '50px',
  }
  const circle_style = {
    backgroundColor: color[props.value],
    borderRadius: '100%',
    paddingTop: "98%"
  }
  const circle = (
    props.value != 0 ? <div style={circle_style}></div> : <div></div>
  )
  return (
    <div style={style}>{circle}</div>
  )
}

function Row(props){
  const style = {
    display: 'inline-block',
  }
  const row = props.row.map((val) => <Cell value={val}/>)
  return (
    <div style={style}>{row}</div>
  )
}

function Board(props){
  return (
    props.board.map((row) => <Row row={row}/>)
  )
}

class App extends React.Component {
  constructor(props){
    super(props)
    this.state = {board: []};
  }

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api'); // fetching the data from api, before the page loaded
      console.log('res', res);
      const data = await res.json();
      console.log('board', data['board']);
      this.setState({board: data['board']});
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <Board board={this.state.board}/>
    )}

}

export default App;
