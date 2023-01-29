import React from 'react';
import $ from 'jquery';

import TaskList from './TaskList';

class Main extends React.Component {

    constructor() {
        super();
        this.state = {
             showModal: false,
             tasks: [
                        {id: 0, name: "Default1", priority: 3},
                        {id: 1, name: "Default2", priority: 1},
                        {id: 2, name: "Default3", priority: 2}
                    ]
        };

        this.updateTasks = this.updateTasks.bind(this);
        this.onDeleteTask = this.onDeleteTask.bind(this);

    }

    componentDidMount() {
         this.updateTasks();
    }

    updateTasks() {

        $.get("/tasks", (data) => {
             this.setState({tasks: data})
             console.log(data)
        });
        console.log('let us go')
        /*
        axios.get(`http://127.0.0.1:5000/tasks`).then(
            res => {
                console.log('attention!')
                console.log(res);

                this.setState({tasks:res})

            },
            error=>{
                console.log(error);
            }
        );

         */

    }



    onDeleteTask(id) {
         $.post("/tasks/delete/" + id, null, () => this.updateTasks());
    }

  render() {
    return (
      <div>
        <h2> My tasks </h2>


        <TaskList tasks={this.state.tasks} onDelete={this.onDeleteTask} />

      </div>
    );
  }
}

export default Main;