import React from 'react'
import ReactDOM from 'react-dom'

import Checkbox from '@material-ui/core/Checkbox'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import Grid from '@material-ui/core/Grid'
import Typography from '@material-ui/core/Typography'

export default class BalancingSet extends React.Component {
  render () {
    const { index, balancing } = this.props

    return (
      <Grid item xs={1}>
        <Checkbox checked={balancing} value={"cell-" +index} />
      </Grid>
    )
  }
}

