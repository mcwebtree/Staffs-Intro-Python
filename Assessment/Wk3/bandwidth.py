# Bandwidth Headache


# inits

m_in_b = int(1000000)
app_a_bw = int(200000)
app_b_bw = int(100000)
app_new_bw = int(350000)

max_bw_M = int(1000 )
max_bw_b = max_bw_M * m_in_b 

conc_users = int(200)

# calcs
current_usage = conc_users * ( app_a_bw + app_b_bw )
free_capacity = max_bw_b - current_usage
new_app_demands = conc_users * app_new_bw
spare_after = max_bw_b - current_usage - new_app_demands 

# outputs
print ( "Bandwidth guesstimator 1000 ")
print ( "-" * 30 )

print ( f'Maximum network bandwidth is { max_bw_b } bps')
print ( f'Current network usage is { current_usage } bps' )
print ( f'Current availability is { free_capacity } bps' )
print ( f'New application requirements are { new_app_demands } bps')
print ( f'Spare Bandwidth available is new app deployed is { spare_after / m_in_b } Mbps ')
