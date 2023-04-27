.. _user_overview:

Overview
========

Creating recipes
----------------

To get the airport name from a given IATA code
you can use the ``airport.get_airport_name(iata_code:str)`` function:

.. py:function:: airport.get_airport_name(iata_code:str)

   Returns an airport name as string.

   :param iata_code: IATA airport code.
   :type kind: str
   :return: Airport name.
   :rtype: str
   :raise lumache.InvalidKindError: If the iata_code is invalid.

The ``iata_code`` parameter should be present in the IATA airport code list.
Otherwise, :py:func:`airport.get_airport_name` will raise an exception.

.. py:exception:: airport.InvalidCodeError

   Raised if the IATA is invalid
