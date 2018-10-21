import React from 'react'
import ReactDOM from 'react-dom'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles'
import Module from './Module'

const styles = theme => ({
  root: {
    flexGrow: 1,
    margin: 32,
  },
  container: {
  },
  module: {
    height: 140,
    width: 100,
  },
  control: {
    padding: 16,
  },
})

class Container extends React.Component {
  render () {
    const { classes, theme } = this.props

    return (
      <Grid container className={classes.root} spacing={16}>
        <Typography component="h2" variant="h2" gutterBottom>
          Battery Modules
        </Typography>
        <Grid item xs={12}>
          <Grid container className={classes.container} justify="center" spacing={16}>
            {[0, 1, 2].map(value => (
              <Module key={value} moduleClassname={classes.module} />
            ))}
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

export default withStyles(styles)(Container)
