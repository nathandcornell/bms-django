import axios from 'axios';
import React from 'react'
import ReactDOM from 'react-dom'

// MaterialUI Components
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'
import { withStyles } from '@material-ui/core/styles'

// Local imports
import Module from './Module'

// Styles
const styles = theme => ({
  root: {
    flexGrow: 1,
    margin: 32,
  },
  container: {
    padding: 16,
  },
  module: {
    padding: 16,
  },
  moduleSection: {
    padding: 8,
  },
  control: {
    padding: 16,
  },
})

class Container extends React.Component {
  constructor (props) {
    super(props)
    this.state = { modules: [] }
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/modules')
    .then(response => {
      this.setState({ modules: response.data });
    })
    .catch(function (error) {
      console.log(error);
    })
  }

  render () {
    const { classes, theme } = this.props

    return (
      <Grid container className={classes.root} spacing={16}>
        <Typography component="h2" variant="h2" gutterBottom>
          Battery Modules
        </Typography>
        <Grid item xs={12}>
          <Grid container className={classes.container} justify="center" spacing={16}>
            {this.state.modules.map(module => (
              <Module
                key={module.serial_no}
                classes={classes}
                data={module}
              />
            ))}
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

export default withStyles(styles)(Container)
