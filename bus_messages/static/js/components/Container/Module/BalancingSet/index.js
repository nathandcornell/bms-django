import React from 'react'
import ReactDOM from 'react-dom'

import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Typography from '@material-ui/core/Typography'

import Cell from './Cell'

export default class GuageSet extends React.Component {
  render () {
    const { classes, data } = this.props
    const cells = [
      data.cell_0_balancing,
      true,
      data.cell_2_balancing,
      data.cell_3_balancing,
      true,
      data.cell_5_balancing,
      data.cell_6_balancing,
    ]

    return (
      <Paper className={classes.moduleSection}>
        <Grid container item xs={10} spacing={16}>
          <Grid item xs={4}>
            <Typography component="h6" variant="h6">Balancing Cells</Typography>
          </Grid>
          {cells.map((value, index) => (
            <Cell key={index} index={index} balancing={value} />
          ))}
        </Grid>
      </Paper>
    )
  }
}
