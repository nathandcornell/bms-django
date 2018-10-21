import React from 'react'
import ReactDOM from 'react-dom'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'

// TODO: Finish this component
export default class Module extends React.Component {
  render () {
    const { key, moduleClassname } = this.props

    return (
      <Grid key={key} item>
        <Paper className={moduleClassname} />
      </Grid>
    )
  }
}
