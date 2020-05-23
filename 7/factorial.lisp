(print "Enter the number factorial to be found:")
(defvar  no (read))
(defun fact(n)
  (if (= n 1)
     1
     (* n (fact( - n 1)))
     )
  )
(setq ans (fact no))
( format t "~% With recursion  ~d " ans)

(setf fact2 1)
(defun facto(n)
  (loop for x from 2 to n
        do(setq fact2 (* x fact2))
        )
  ( format t "~% Without  recursion  ~d " fact2)
  )
(facto no)

