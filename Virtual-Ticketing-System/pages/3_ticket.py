import streamlit as st
import random

class StadiumBookingSystem:
    def __init__(self):
        self.total_income = 0
        self.total_seats = 0
        self.booked_seats = 0
        self.booked_ticket_person = []
        self.seat_chart = []
        self.matches_cricket = {}
        self.matches_basketball = {}
        self.matches_football = {}

    def add_match_cricket(self, match_name, match_function):
        self.matches_cricket[match_name] = match_function

    def add_match_basketball(self, match_name, match_function):
        self.matches_basketball[match_name] = match_function

    def add_match_football(self, match_name, match_function):
        self.matches_football[match_name] = match_function

    def book_tickets(self, match_name, num_seats):
        st.write(f"Booking {num_seats} tickets for {match_name}...")
        # Placeholder for booking logic
        pass

    def store_booking_details(self, match_name, num_seats, user_details):
        # Placeholder for storing booking details
        pass

    def collect_user_details(self):
        user_details = {}
        user_details['Name'] = st.text_input("Enter your name:")
        user_details['Email'] = st.text_input("Enter your email:")
        user_details['Phone'] = st.text_input("Enter your phone number:")
        return user_details

    def main(self):
        # Add cricket matches
        self.add_match_cricket("Cricket Match 1 - Today, 7:30 pm", self.book_tickets)
        self.add_match_cricket("Cricket Match 2 - Tomorrow, 7:30 pm", self.book_tickets)
        self.add_match_cricket("Cricket Match 3 - May 3rd, 7:30 pm", self.book_tickets)
        self.add_match_cricket("Cricket Match 4 - May 4th, 7:30 pm", self.book_tickets)
        self.add_match_cricket("Cricket Match 5 - May 5th, 7:30 pm", self.book_tickets)

        # Add basketball matches
        self.add_match_basketball("Basketball Match 1 - Today, 8:00 pm", self.book_tickets)
        self.add_match_basketball("Basketball Match 2 - Tomorrow, 8:00 pm", self.book_tickets)
        self.add_match_basketball("Basketball Match 3 - May 3rd, 8:00 pm", self.book_tickets)
        self.add_match_basketball("Basketball Match 4 - May 4th, 8:00 pm", self.book_tickets)
        self.add_match_basketball("Basketball Match 5 - May 5th, 8:00 pm", self.book_tickets)

        # Add football matches
        self.add_match_football("Football Match 1 - Today, 8:30 pm", self.book_tickets)
        self.add_match_football("Football Match 2 - Tomorrow, 8:30 pm", self.book_tickets)
        self.add_match_football("Football Match 3 - May 3rd, 8:30 pm", self.book_tickets)
        self.add_match_football("Football Match 4 - May 4th, 8:30 pm", self.book_tickets)
        self.add_match_football("Football Match 5 - May 5th, 8:30 pm", self.book_tickets)

        # Display available matches and allow the user to select a match
        st.write("## CRICKET MATCHES")
        selected_cricket_match = st.selectbox("Select a cricket match to book tickets for:", list(self.matches_cricket.keys()))
        if st.button("Select Cricket Match"):
            match_selected = self.matches_cricket[selected_cricket_match]
            num_seats = st.number_input("Enter the number of seats:", min_value=1, max_value=10, value=1)
            match_selected(selected_cricket_match, num_seats)

        st.divider()
        st.write("## BASKETBALL MATCHES")
        selected_basketball_match = st.selectbox("Select a basketball match to book tickets for:", list(self.matches_basketball.keys()))
        if st.button("Select Basketball Match"):
            match_selected = self.matches_basketball[selected_basketball_match]
            num_seats = st.number_input("Enter the number of seats:", min_value=1, max_value=10, value=1)
            match_selected(selected_basketball_match, num_seats)

        st.divider()
        st.write("## FOOTBALL MATCHES")
        selected_football_match = st.selectbox("Select a football match to book tickets for:", list(self.matches_football.keys()))
        if st.button("Select Football Match"):
            match_selected = self.matches_football[selected_football_match]
            num_seats = st.number_input("Enter the number of seats:", min_value=1, max_value=10, value=1)
            match_selected(selected_football_match, num_seats)

        st.divider()

        # Display the booking options
        prize_of_ticket = 0
        Total_Income = 0
        Row = st.sidebar.number_input('Enter number of Row', min_value=1, value=5, key='row_input')
        Seats = st.sidebar.number_input('Enter number of seats in a Row', min_value=1, value=10, key='seats_input')
        Total_seat = Row * Seats
        Booked_seat = 0
        Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]

        class Chart:
            @staticmethod
            def chart_maker(Booked_seat):
                seats_chart = {}
                for i in range(Row):
                    seats_in_row = {}
                    for j in range(Seats):
                        if j < 10:  # Select only first 10 seats randomly
                            if random.random() < 0.5:  # Randomly select seats with 50% probability
                                seats_in_row[str(j+1)] = 'B'  # Booked seat
                                Booked_seat += 1
                            else:
                                seats_in_row[str(j+1)] = 'S'  # Empty seat
                        else:
                            seats_in_row[str(j+1)] = 'S'  # Rest of the seats are empty
                    seats_chart[str(i)] = seats_in_row
                return seats_chart, Booked_seat

            @staticmethod
            def find_percentage(Booked_seat):
                percentage = (Booked_seat/Total_seat)*100
                return percentage

        class_call = Chart

        x = 1  # Set default option to 2 for seat selection
        option_counter = 0  # Counter for generating unique keys
        while x != 0:
            option_counter += 1
            option_key = f'option_input_{option_counter}'  # Generate unique key
            
            st.write("   ")
            st.write("   ")
            st.write("   ")
            st.title("Booking")
            st.write('1-for Select Randomly \n')
            st.write('2-for Seat selection \n')
            st.write('3-to show booked tickets user info \n')
            st.write('0-for exit \n')
            x = st.number_input('Select Option', min_value=0, max_value=4, step=1, key=option_key)
    
    # Rest of your code...


            if x == 1:
                st.write('Stadium View:')
                table_of_chart, Booked_seat = class_call.chart_maker(Booked_seat)
                for i in range(Row):
                    row_seats = ''
                    for j in range(Seats):
                        if table_of_chart[str(i)][str(j+1)] == 'S':
                            row_seats += '◻️ '  # Empty seat
                        else:
                            row_seats += '◼️ '  # Booked seat
                    st.write(row_seats)
                st.write('Selecting Randomly...')
                st.write('Proceed to payment details')
                # Placeholder for payment details

            elif x == 2:
                st.write('Selecting Seats Row and Column Wise:')
                Row_number = st.number_input('Enter Row Number', min_value=1, max_value=Row, key='row_number_input_2')  # Change key here
                Column_number = st.number_input('Enter Column Number', min_value=1, max_value=Seats, key='column_number_input_2')  # Change key here
                st.write('Stadium View:')
                table_of_chart, Booked_seat = class_call.chart_maker(Booked_seat)
                for i in range(Row):
                    row_seats = ''
                    for j in range(Seats):
                        if table_of_chart[str(i)][str(j+1)] == 'S':
                            row_seats += '◻️ '  # Empty seat
                        else:
                            row_seats += '◼️ '  # Booked seat
                    st.write(row_seats)
                if Row_number in range(1, Row+1) and Column_number in range(1, Seats+1):
                    if table_of_chart[str(Row_number-1)][str(Column_number)] == 'S':
                        if Row*Seats <= 60:
                            prize_of_ticket = 10
                        elif Row_number <= int(Row/2):
                            prize_of_ticket = 5000
                        else:
                            prize_of_ticket = 500
                        st.write('prize_of_ticket - ', '$', prize_of_ticket)
                        conform = st.selectbox('Booking Confirmation', ['yes', 'no'], key='confirmation_input_2')  # Change key here
                        person_detail = {}
                        if conform == 'yes':
                            person_detail['Name'] = st.text_input('Enter Name', key='name_input_2')  # Change key here
                            person_detail['Gender'] = st.selectbox('Select Gender', ['Male', 'Female', 'Other'], key='gender_input_2')  # Change key here
                            person_detail['Age'] = st.number_input('Enter Age', min_value=1, key='age_input_2')  # Change key here
                            person_detail['Phone_No'] = st.text_input('Enter Phone number', key='phone_input_2')  # Change key here
                            person_detail['Payment Method'] = st.selectbox('Payment Method', ['Credit Card', 'Debit Card', 'PayPal'], key='payment_method_input_2')  # Change key here
                            person_detail['Card Number'] = st.text_input('Enter Card Number', key='card_number_input_2')  # Change key here
                            person_detail['Expiry Date'] = st.text_input('Enter Expiry Date', key='expiry_date_input_2')  # Change key here

                            payment_done = st.checkbox('Payment Done')
                            if payment_done:
                                # Check if all details are entered
                                if all(person_detail.values()):
                                    table_of_chart[str(Row_number-1)][str(Column_number)] = 'B'
                                    Booked_seat += 1
                                    Total_Income += prize_of_ticket
                                    st.success('Booking Successfully')
                                else:
                                    st.warning("Please enter all details to proceed with booking.")
                            else:
                                st.warning('Payment not completed. Booking unsuccessful.')

                        else:
                            continue
                        Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
                        st.button("Submit")
                        
                    else:
                        st.error('This seat already booked by someone')
                else:
                    st.error('***    ***')

            elif x == 3:
                st.write('Number of purchased Ticket - ', Booked_seat)
                st.write('Percentage - ', class_call.find_percentage(Booked_seat))
                st.write('Current  Income - ', '$', prize_of_ticket)
                st.write('Total Income - ', '$', Total_Income)

            elif x == 4:
                st.write('Show booked Tickets User Info:')
                # Placeholder for displaying booked tickets user info

            else:
                st.error('***   ***')

if __name__ == "__main__":
    stadium_booking_system = StadiumBookingSystem()
    stadium_booking_system.main()
